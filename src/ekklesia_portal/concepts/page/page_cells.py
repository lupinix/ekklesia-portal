from ekklesia_portal.concepts.ekklesia_portal.cell.layout import LayoutCell
from ekklesia_portal.concepts.ekklesia_portal.cell.form import NewFormCell, EditFormCell
from ekklesia_portal.database.datamodel import Page
from ekklesia_portal.permission import CreatePermission, EditPermission
from .pages import Pages


class PagesCell(LayoutCell):
    model = Pages

    def pages(self):
        return list(self._model.pages(self._request.q))

    # Methods from this class can be called from the template.

    # Methods with only the self argument can be used without call parentheses and their result value is cached.
    def show_new_button(self):
        return self.options.get('show_new_button') and self._request.permitted_for_current_user(self._model, CreatePermission)


class PageCell(LayoutCell):
    model = Page

    # Model attributes included here are available as variables in the template:
    # = name
    model_properties = ['lang', 'name', 'text', 'title']

    def can_edit(self):
        return self._request.permitted_for_current_user(self._model, EditPermission)

    def show_edit_button(self):
        return self.options.get('show_edit_button') and self.can_edit


class NewPageCell(NewFormCell):
    pass

    # def _prepare_form_for_render(self):
        # By default, the form's prepare_for_render() method is called without arguments.
        # You can pass additional args, for example to set values for select fields like this:

        # items = items_for_page_select_widgets(self._model)
        # self._form.prepare_for_render(items)


class EditPageCell(EditFormCell):
    pass

    # def _prepare_form_for_render(self):
        # By default, all fields from the model as given by to_dict() are passed to the form.
        # You can customize the behaviour (inherited from the base class) here:

        # form_data = self._model.to_dict()
        # self.set_form_data(form_data)

        # By default, the form's prepare_for_render() method is called without arguments.
        # You can pass additional args, for example to set values for select fields like this:

        # items = items_for_page_select_widgets(self._model)
        # self._form.prepare_for_render(items)
