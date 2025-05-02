from ..extensions import StringField, FlaskForm, TextAreaField, SubmitField, DataRequired


class CreateBlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    tags = StringField('Tags (comma-separated)')
    submit = SubmitField('Create Post')


class EditBlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    tags = StringField('Tags (comma-separated)')
    submit = SubmitField('Update Post')