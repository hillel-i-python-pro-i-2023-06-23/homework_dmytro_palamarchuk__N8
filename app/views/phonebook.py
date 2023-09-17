"""phone book number"""

from flask import Blueprint, render_template, redirect, url_for, flash
from app.services.db_connection import DBConnection, create_table

from app.forms.phone_form import PhoneForm


phonebook = Blueprint("phonebook", __name__)


@phonebook.route("/create", methods=["GET", "POST"])
def create() -> render_template:
    """Create a new phone"""
    form = PhoneForm()

    if form.validate_on_submit():
        # Process the form data here
        query = "INSERT INTO 'phones' ('contact_name', 'phone_value') VALUES (?, ?)"
        values = (form.name.data, form.phone_number.data)

        with DBConnection() as connection:
            with connection:
                connection.execute(query, values)
        flash("Phone number stored successfully", "success")
        return redirect(url_for("phonebook.phone_list"))

    return render_template("phonebook/phone_create.html", form=form)


@phonebook.route("/get/<int:phone_id>", methods=["GET"])
def get(phone_id: int) -> render_template:
    """
    Get a phone record by its ID.

    Args:
        phone_id (int): The ID of the phone record to retrieve.

    Returns:
        render_template: Renders the "phone_view.html" template with the retrieved phone record.
    """
    query = "SELECT * FROM phones WHERE phone_id = ?"
    values = (phone_id,)
    with DBConnection() as connection:
        with connection:
            contact = connection.execute(query, values).fetchone()
    return render_template("phonebook/phone_view.html", contact=contact)


@phonebook.route("/update/<int:phone_id>", methods=["GET", "POST"])
def update(phone_id: int) -> render_template:
    """Update a phone"""
    query = "SELECT * FROM phones WHERE phone_id = ?"
    values = (phone_id,)
    with DBConnection() as connection:
        with connection:
            contact = connection.execute(query, values).fetchone()

    if contact is not None:
        form = PhoneForm(name=contact[1], phone_number=contact[2])

        if form.validate_on_submit():
            # Process the form data here
            query = (
                "UPDATE phones SET contact_name = ?, phone_value = ? WHERE phone_id = ?"
            )
            values = (form.name.data, form.phone_number.data, phone_id)

            with DBConnection() as connection:
                with connection:
                    connection.execute(query, values)
            flash("Phone number stored successfully", "success")
            return redirect(url_for("phonebook.get", phone_id=phone_id))

        return render_template("phonebook/phone_update.html", form=form)

    flash("Phone number is undefined", "success")
    return redirect(url_for("phonebook.phone_list"))


@phonebook.route("/delete/<int:phone_id>", methods=["GET"])
def delete(phone_id: int) -> render_template:
    """Delete a phone"""

    query = "DELETE FROM phones WHERE phone_id = ?"
    values = (phone_id,)

    with DBConnection() as connection:
        with connection:
            connection.execute(query, values)

    flash("Phone number deleted successfully", "success")
    return redirect(url_for("phonebook.phone_list"))


@phonebook.route("/")
@phonebook.route("/all")
def phone_list() -> render_template:
    """Get all phones"""
    query = "SELECT * FROM phones"
    with DBConnection() as connection:
        with connection:
            data = connection.execute(query).fetchall()

    return render_template("phonebook/index.html", data=data)


create_table()
