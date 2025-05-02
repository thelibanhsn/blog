from datetime import datetime
from ..extensions import db

blog_tags = db.Table('blog_tags',
    db.Column('blog_id', db.Integer, db.ForeignKey('blog.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    # Foreign key — user who created this blog
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationship with tags
    tags = db.relationship('Tag', secondary=blog_tags, lazy='subquery',
                           backref=db.backref('blogs', lazy=True))
    
    def __init__(self, title, content, author_id, author_name):
        self.title = title
        self.content = content
        self.author_id = author_id
        self.author_name = author_name

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update():
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
