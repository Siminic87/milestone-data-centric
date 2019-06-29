import os
from flask import Flask, render_template, redirect, request, url_for, request, session, Blueprint, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime
from datetime import date, timedelta

from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
from flask_paginate import Pagination, get_page_parameter, get_page_args
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'user_tips'
app.config["MONGO_URI"] = 'mongodb://admin:g00gle@ds121636.mlab.com:21636/user_tips'

app.secret_key = os.urandom(24)

mongo = PyMongo(app)

mod = Blueprint('tips', __name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = ''
app.config['SECRET_KEY'] = "lkkajdghdadkglajkgah"

# User Registration
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class User(UserMixin):
  def __init__(self,id):
    self.id = id

@app.route('/login/')
def login():
    login_user(User(1))
    return redirect(url_for('all_categories'))

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('all_categories'))

@app.route("/user_tips/tips")
def user_tips_tips():
    tips = mongo.db.tips.find()
    json_tips = []
    for tip in tips:
        json_tips.append(tip)
    json_tips = json.dumps(json_tips, default=json_util.default)
    return json_tips

@app.route("/summary")
def summary():
    return render_template('summary.html')

# Routes
@app.route('/')
def all_categories():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    
    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page

    tips = mongo.db.tips.find().sort("upvotes", -1).limit(per_page).skip(offset)
    pagination = Pagination(page=page, per_page=per_page, offset=offset, total=mongo.db.tips.count(), search=search, record_name='tips')
    # 'page' is the default name of the page parameter, it can be customized
    # e.g. Pagination(page_parameter='p', ...)
    # or set PAGE_PARAMETER in config file
    # also likes page_parameter, you can customize for per_page_parameter
    # you can set PER_PAGE_PARAMETER in config file
    # e.g. Pagination(per_page_parameter='pp')

    datenew = str(datetime.date.today().strftime('%d %B, %Y'))

    return render_template('tips.html',
                           tips=tips,
                           pagination=pagination,
                           categories=mongo.db.categories.find(),
                           category=mongo.db.categories.find(),
                           all=mongo.db.tips.count(),
                           datenew=datenew,
                           new=mongo.db.tips.find({"date": datenew}).count())
        
@app.route('/<category>', methods=['POST','GET'])
def sort_by_category(category):
    search = False
    q = request.args.get('q')
    if q:
        search = True
    
    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page
    
    tips=mongo.db.tips.find({"category_name" : category}).sort("upvotes", -1).limit(per_page).skip(offset)
    categories=mongo.db.categories.find()
    pagination = Pagination(page=page, per_page=per_page, offset=offset, total=mongo.db.tips.find({"category_name" : category}).count(), search=search, record_name='tips')
    
    return render_template("category.html",
    tips=tips,
    pagination=pagination,
    categories=categories,
    category=category,
    all=mongo.db.tips.find({"category_name" : category}).count(),
    new=mongo.db.tips.find({"category_name" : category,
                            "date": str(datetime.date.today().strftime('%d %B, %Y'))}).count())
    
@app.route('/detail/<tip_id>', methods=['GET'])
def tip_detail(tip_id):
    the_tip = mongo.db.tips.find_one({"_id": ObjectId(tip_id)})
    
    return render_template("tipdetail.html",
    all=1,
    new=mongo.db.tips.find({"date": str(datetime.date.today().strftime('%d %B, %Y'))}).count(),
    tip=the_tip)
    
# Upvoting
@app.route('/upvote/<tip_id>', methods=['GET'])
def upvote(tip_id):
    if mongo.db.tips.find({'_id': ObjectId(tip_id),
                           "user_id" : current_user}).exists():

        flash('You already upvoted this!')
        return redirect(url_for('all_categories'))

    else:
        mongo.db.tips.find_one_and_update(
            {'_id': ObjectId(tip_id)},
            {'$inc': {'upvotes': int(1)}})
    return redirect(url_for('all_categories'))
    
@app.route('/upvote-detail/<tip_id>', methods=['GET'])
def upvote_detail(tip_id):
    mongo.db.tips.find_one_and_update(
        {'_id': ObjectId(tip_id)},
        {'$inc': {'upvotes': int(1)}})
    return redirect(url_for('tip_detail', tip_id=tip_id))

@app.route('/upvote/<category>/<tip_id>', methods=['GET'])
def upvote_category(category, tip_id):
    
    mongo.db.tips.find_one_and_update(
        {'_id': ObjectId(tip_id)},
        {'$inc': {'upvotes': int(1)}})
    return redirect(url_for('sort_by_category', category=category))
    
# Downvoting
@app.route('/downvote/<tip_id>', methods=['GET'])
def downvote(tip_id):
    mongo.db.tips.find_one_and_update(
        {'_id': ObjectId(tip_id)},
        {'$inc': {'upvotes': int(-1)}})
    return redirect(url_for('all_categories'))
    
@app.route('/downvote-detail/<tip_id>', methods=['GET'])
def downvote_detail(tip_id):
    mongo.db.tips.find_one_and_update(
        {'_id': ObjectId(tip_id)},
        {'$inc': {'upvotes': int(-1)}})
    return redirect(url_for('tip_detail', tip_id=tip_id))

@app.route('/downvote/<category>/<tip_id>', methods=['GET'])
def downvote_category(category, tip_id):
    mongo.db.tips.find_one_and_update(
        {'_id': ObjectId(tip_id)},
        {'$inc': {'upvotes': int(-1)}})
    return redirect(url_for('sort_by_category', category=category))
    
@app.route('/downvote/<tip_id>')
def downvote_sorted(tip_id):
    
    category = session.get('category', None)
    
    mongo.db.tips.find_one_and_update(
        {'_id': ObjectId(tip_id)},
        {'$inc': {'upvotes': int(-1)}})
    return redirect(url_for('sort_by_category', category=category))
    
@app.route('/add_tip')
@login_required
def add_tip():
    return render_template("addtip.html",
    categories=mongo.db.categories.find())
    
@app.route('/insert_tip', methods=['POST'])
def insert_tip():
    tips = mongo.db.tips
    tips.insert_one(
        {
            'tip_name': request.form.get('tip_name'), 
            'category_name': request.form.get('category_name'), 
            'tip_description': request.form.get('tip_description'), 
            'date': request.form.get('date'), 
            'upvotes': 0
        })
    return redirect(url_for('all_categories'))
    
@app.route('/edit_tip/<tip_id>')
def edit_tip(tip_id):
    the_tip = mongo.db.tips.find_one({"_id": ObjectId(tip_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edittip.html', tip=the_tip, categories=all_categories)
    
@app.route('/update_tip/<tip_id>', methods=["POST"])
def update_tip(tip_id):
    tips = mongo.db.tips
    upvotes = mongo.db.tips.find_one({'_id': ObjectId(tip_id)}, {"upvotes": True, "_id": False})
    tips.update( {'_id': ObjectId(tip_id)},
    {
        'tip_name':request.form.get('tip_name'),
        'category_name':request.form.get('category_name'),
        'tip_description': request.form.get('tip_description'),
        'date': request.form.get('date'),
        'upvotes': upvotes["upvotes"],
    })
    return redirect(url_for('all_categories'))
    
@app.route('/delete_tip/<tip_id>')
def delete_tip(tip_id):
    mongo.db.tips.remove({'_id': ObjectId(tip_id)})
    return redirect(url_for('all_categories'))
    
@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
    categories=mongo.db.categories.find())
    
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))
    
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))
    
@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form['category_name']})
    return redirect(url_for('get_categories'))
    
@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    category_doc = {'category_name': request.form['category_name']}
    categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))
    
@app.route('/new_category')
def new_category():
    return render_template('addcategory.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)