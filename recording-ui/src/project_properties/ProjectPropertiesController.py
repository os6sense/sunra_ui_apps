"""
ProjectPropertiesController - see class defination for documentation
"""
#import pytz
#from dateutil.parser import parse
from datetime import datetime

from PyQt4.QtCore import QObject, SIGNAL, QTime

from PyQt4.QtGui import QMessageBox#, QIcon

from config import Config
from sunra.recording_db_proxy import RecordingDBProxy

from .ProjectPropertiesModel import ProjectPropertiesModel
from .ProjectPropertiesFormView import ProjectPropertiesFormView
from .ProjectPropertiesListView import ProjectPropertiesListView

from i18n.translate import _
from sunra.presenters import TimePresenter

###############################################################################
# ProjectPropertiesController
###############################################################################
class ProjectPropertiesController(QObject):
    """
    Controller for the project properties dialog interaction.
    Based on the presence of exisiting projects (projects being returned
    via the RecordingDBProxy), the form controller will chose to display
    either the list view or the form view.

    Once a valid project has either been selected or created the controller
    will emit a ShowRecorder signal.
    """
    def __init__(self):
        super(ProjectPropertiesController, self).__init__(None)

        self.config = Config()
        self.rdb_proxy = RecordingDBProxy(self.config)

        self.pp_form_view = ProjectPropertiesFormView()
        self.pp_list_view = ProjectPropertiesListView()

        # _form will hold a reference with to a listview or a formview
        self._form = None

        # Wire up the list view
        self.pp_list_view.connect(self.pp_list_view,
                SIGNAL("ProjectSelected"), self.select_project)
        self.pp_list_view.connect(self.pp_list_view,
                SIGNAL("NewProject"), self.new_project)
        self.pp_list_view.connect(self.pp_list_view,
                SIGNAL("Cancelled"), self.cancelled)

        # Wire up the form view
        self.pp_form_view.connect(self.pp_form_view,
                SIGNAL("CreateProject"), self.create_project)
        self.pp_form_view.connect(self.pp_form_view,
                SIGNAL("UpdateProject"), self.update_project)
        self.pp_form_view.connect(self.pp_form_view,
                SIGNAL("Cancelled"), self.cancelled)

    def set_default_times(self):
        """
        Set sensible defaults for the time values based on the current
        time.
        """
        # The majority of bookings happen between 5pm and 11pm so we use these
        # as sensible defaults.
        self.pp_form_view.endTime = QTime(23, 0)
        self.pp_form_view.startTime = QTime(17, 0)

        # however if this is being setup pre 9am its almost definately an
        # 1/2 or all day booking.
        now = datetime.now()

        if now < now.replace(hour=12, minute=0, second=0):
            self.pp_form_view.endTime = QTime(17, 0)
            self.pp_form_view.startTime = QTime(now.hour+1, 0)

    def show(self):
        """
        Determines which dialog to show depending on whether there is either
        a booking in progress, or if there is a later booking.
        """
        try:
            self.projects = self.rdb_proxy.get_todays_bookings()
        except Exception, e:
            self.projects = {'exception': True, 'error': str(e)}

        print type(self.projects)
        print self.projects

        if len(self.projects) > 0:
            # Check for an error field
            if ((type(self.projects) is dict and self.projects.has_key('error')) or \
                (type(self.projects) is list and self.projects[0].has_key('error'))):

                print "DEBUG: projects = %s" % self.projects
                self.pp_list_view.showErrors(_("Error Obtaining Booking Details"),
                     ["Exiting because the system could not connect to REST API" +
                     "- check the API key in /etc/sunra/config.yml.\n\n" +
                     "The actual error message was: \n\n%s" % self.projects['error']])
                exit(100)

            # there are existing bookings, show them and allow the user to
            # choose whether to use a current or future booking
            form = self.pp_list_view
            form.add_projects(self.projects)
        else:
            self.set_default_times()
            form = self.pp_form_view

        self._form = form

        form.studio_name_label.setText(self.config.studio_name)
        form.date_label.setText(datetime.now().strftime("TODAY %d-%m-%y"))

        form.show()

    def new_project(self):
        """
        Show a blank PropectPropertiesFormView dialog for creating
        a new project.
        """
        self.set_default_times()
        self.pp_list_view.hide()
        self.pp_form_view.show()

    def select_project(self, model):
        """
        Show the ProjectPropertiesFormView and populate it with information
        from the ProjectPropertiesListView.
        """
        self.pp_list_view.hide()
        self.emit(SIGNAL("ShowRecorder"),
                ProjectPropertiesModel(model[0], model[1]))

    def _prompt_use_existing_project(self, errors, model):
        """
        Helper, tidies up create_project.
        """
        question_text = _("The client '%s', already has a project named '%s'" \
            ". Would you like to use this project? ") \
            % (model.client_name, model.project_name)

        if "\n".join("".join(item[1]) for item in errors.items()
                ).find("already been taken") > 0:

            if  self._form.showQuestion(_("Project Exists"),
                    question_text) == QMessageBox.No:
                return False

            return True

    def _create_model_from_form(self, form):
        """
        Helper, return a ProjectPropertiesModel based on the values in
        the form.

        Params
        +form+:: It really only makes sense if this is an instance of
        PropectPropertiesFormView but any object which responds to client_name,
        project_title, startTime and endTime will do. (hmmmm funky naming
        there TODO: )
        """
        model = ProjectPropertiesModel()
        model.client_name = form.client_name
        model.project_name = form.project_title
        model.date = datetime.now()

        model.start_time = form.startTime
        model.end_time = form.endTime

        return model

    def _confirm_project_settings(self, model):
        """
        Prompt for confirmation, showing the user the settings they have
        specified for the project. It is *hoped* that this will reduce errors
        in the setup of projects, especially for the time of the booking.
        """
        question_text = _(
                "You are about to create a project with the details:\n\n" \

                "Project Name  : %s\n" \
                "Client Name   : %s\n\n" \

                "Start Time    : %s\n" \
                "End Time      : %s\n\n" \

                "ARE THESE DETAILS CORRECT? ") \
            % (model.client_name, model.project_name,
                    TimePresenter(model.start_time.time()),
                    TimePresenter(model.end_time.time())
        )


        response = self._form.showQuestion(_("Project Exists"), question_text)
        if response == QMessageBox.No:
            return False

        return True

    def create_project(self):
        """
        Create a new project and booking via the rails api.
        """
        model = self._create_model_from_form(self.pp_form_view)
        errors = model.verify(self.projects)

        if len(errors) > 0:
            self._form.showErrors("Please correct the following errors", errors)
            return

        # Ask the user to confirm the propect settings
        if not self._confirm_project_settings(model):
            return

        # if there are errors with creating the project they will be returned
        # as an array
        errors = model.create_project(self.rdb_proxy)

        if errors != None:
            # If there are errors it is likely to be because there is an
            # existing project which the settings clash with
            if self._prompt_use_existing_project(errors, model):
                model.uuid = self.rdb_proxy.find_project(model.client_name,
                    model.project_name)
            else:
                return

        # We *should* have a model with a valid uuid for a project at  this
        # point, if not show an error and return
        if model.uuid <= 0:
            msg = _("Could not create or obtain project id - unrecoverable " \
                    "internal error. (This shouldn't happen of course)")

            self._form.showError("There Were Errors", msg)
            return

        # attempt to create a booking
        errors = model.create_booking(self.rdb_proxy)
        if errors != None:
            self._form.showErrors("Could Not Create Booking", errors)
            return

        # We had no errors but we dont have a booking_id. The technical term
        # if this happens is WTF?
        if model.booking_id <= 0:
            msg = _("Could not create or obtain booking id - unrecoverable " \
                    "internal error. (This shouldn't happen of course)")

            self._form.showErrors(_("There Were Errors"), msg)
            return

        # Hide the forms and switch to the recorder window via the application
        # controller
        self.pp_list_view.hide()
        self.pp_form_view.hide()
        self.emit(SIGNAL("ShowRecorder"), model)

    def update_project(self, model):
        """
        Responds to an UpdateProject signal from the view.
        """
        model.update()

    def cancelled(self):
        """
        Responds to a cancelled event from the views.
        """
        self.pp_list_view.close()
        self.pp_form_view.close()

