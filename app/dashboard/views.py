from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import login_required, current_user, db
from .models import Blog, Tag
from .forms import CreateBlogForm, EditBlogForm
from ..auth.models import User

dashboard_bp = Blueprint('dashboard_bp', __name__, url_prefix='/admin', template_folder='templates')

@dashboard_bp.route('/dashboard/')
@login_required
def index():
    blogs = Blog.query.all()
    tags = Tag.query.all()
    return render_template('index.html', blogs=blogs, tags=tags)

# get blog detail
@dashboard_bp.route('/blog/<int:blog_id>/')
def blog_detail(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    return render_template('blog_detail.html', blog=blog)

@dashboard_bp.route('/create-blog/', methods=['GET', 'POST'])
@login_required
def create_blog():
    form = CreateBlogForm()
    if form.validate_on_submit():
        blog = Blog(title=form.title.data, content=form.content.data, author_id = current_user.id)
        
        # Split tags by comma and strip whitespace
        tags = form.tags.data.split(',') if form.tags.data else []
        blog.tags = [Tag(name=tag.strip()) for tag in tags]
        
        
        Blog.save(blog)
        flash('blog created successfully!', 'success')
        return redirect(url_for('dashboard_bp.index'))
    return render_template('create_blog.html', form=form)

# Edit blog
@dashboard_bp.route('/edit-blog/<int:blog_id>/', methods=['GET', 'POST'])
@login_required
def edit_blog(blog_id):
    form = EditBlogForm()
    blog = Blog.query.get_or_404(blog_id)
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.content = form.content.data
        
        # Split tags by comma and strip whitespace
        tags = form.tags.data.split(',') if form.tags.data else []
        blog.tags = [Tag(name=tag.strip()) for tag in tags]
        
        Blog.update()
        flash('blog updated successfully!', 'success')
        return redirect(url_for('dashboard_bp.index'))
    
    form.content.data = blog.content
    return render_template('edit_blog.html', form=form, blog=blog)


# Delete blog
@dashboard_bp.route('/delete-blog/<int:blog_id>/')
@login_required
def delete_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    Blog.delete(blog)
    flash('blog deleted successfully!', 'success')
    return redirect(url_for('dashboard_bp.index'))

