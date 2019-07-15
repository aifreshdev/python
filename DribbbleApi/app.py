import config
from module import app, upload
from flask import url_for, render_template, jsonify

@app.route('/user/projects')
def userProjects():
	data = [
	  {
	    "id" : 3,
	    "name" : "Web Standards Sherpa",
	    "description" : "I did visual design and art direction for this project, working with the <a href=\"http://webstandards.org\">Web Standards Project</a> and Microsoft.",
	    "shots_count" : 4,
	    "created_at" : "2011-04-14T03:43:47Z",
	    "updated_at" : "2012-04-04T22:39:53Z"
	  }
	]

	return jsonify(data)

@app.route('/user/shots')
def userShots():
	data = [
		  {
		    "id" : 471756,
		    "title" : "Sasquatch",
		    "description" : "<p>Quick, messy, five minute sketch of something that might become a fictional something.</p>",
		    "width" : 400,
		    "height" : 300,
		    "images" : {
		      "hidpi" : None,
		      "normal" : "https://d13yacurqjgara.cloudfront.net/users/1/screenshots/471756/sasquatch.png",
		      "teaser" : "https://d13yacurqjgara.cloudfront.net/users/1/screenshots/471756/sasquatch_teaser.png"
		    },
		    "published_at" : "2012-03-15T01:52:33Z",
		    "updated_at" : "2012-03-15T02:12:57Z",
		    "html_url" : "https://dribbble.com/shots/471756-Sasquatch",
		    "animated" : False,
		    "tags" : [
		      "fiction",
		      "sasquatch",
		      "sketch",
		      "wip"
		    ],
		    "attachments" : [
		      {
		        "id" : 206165,
		        "url" : "https://d13yacurqjgara.cloudfront.net/users/1/screenshots/1412410/attachments/206165/weathered-ball-detail.jpg",
		        "thumbnail_url" : "https://d13yacurqjgara.cloudfront.net/users/1/screenshots/1412410/attachments/206165/thumbnail/weathered-ball-detail.jpg",
		        "size" : 116375,
		        "content_type" : "image/jpeg",
		        "created_at" : "2014-02-07T16:35:09Z"
		      }
		    ],
		    "projects" : [
		      {
		        "id" : 3,
		        "name" : "Web Standards Sherpa",
		        "description" : "I did visual design and art direction for this project, working with the <a href=\"http://webstandards.org\">Web Standards Project</a> and Microsoft.",
		        "shots_count" : 4,
		        "created_at" : "2011-04-14T03:43:47Z",
		        "updated_at" : "2012-04-04T22:39:53Z"
		      }
		    ],
		    "team" : {
		      "id" : 39,
		      "name" : "Dribbble",
		      "login" : "dribbble",
		      "html_url" : "https://dribbble.com/dribbble",
		      "avatar_url" : "https://d13yacurqjgara.cloudfront.net/users/39/avatars/normal/apple-flat-precomposed.png?1388527574",
		      "bio" : "Show and tell for designers. This is Dribbble on Dribbble.",
		      "location" : "Salem, MA",
		      "links" : {
		        "web" : "http://dribbble.com",
		        "twitter" : "https://twitter.com/dribbble"
		      },
		      "type" : "Team",
		      "created_at" : "2009-08-18T18:34:31Z",
		      "updated_at" : "2014-02-14T22:32:11Z"
		    },
		    "low_profile" : False
		  }
		]

	return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=config.DEBUG)