"""Phone create and update form"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TelField
from wtforms.validators import DataRequired, Length, ValidationError
from phonenumbers import parse, is_valid_number, phonenumberutil


class PhoneForm(FlaskForm):
    """
    Form for creating a new or update phone record.
    """

    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=50)])
    phone_number = TelField("Phone", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def validate_phone_number(self, phone_number):
        """
        Checks whether the phone number entered is a valid number.

        :param phone_number: Phone number.
        :type phone_number: str
        :raises: ValidationError, if the phone number is invalid..
        """

        try:
            phone = parse("+" + phone_number.data, None)

            if not is_valid_number(phone):
                raise ValueError()
        except (phonenumberutil.NumberParseException, ValueError) as exc:
            raise ValidationError("Invalid phone number") from exc
