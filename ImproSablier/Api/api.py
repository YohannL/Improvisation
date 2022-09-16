from Libs.Controller.controllerEvent import ControllerEvent
from flask import Flask, jsonify, request

from Libs.Controller.controllerModel import ControllerModel
 
ApiApp = Flask(__name__)

# STD API ROUT ==================================================================
@ApiApp.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@ApiApp.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

# POST API ======================================================================

@ApiApp.route('/api/v1/admin/status/<status>', methods=['POST'])
def admin_changeStatus(status):
    try: 
        
        response = ControllerEvent().admin_changeStatus(status)
        return jsonify(status=200)
    except:
        return jsonify(status=400, message = "Error")

@ApiApp.route('/api/v1/admin/timer/add/<player>', methods=['POST'])
def admin_addTime(player):
    try: 
        response = ControllerEvent().admin_addTime(player)
        return jsonify(status=200)
    except:
        return jsonify(status=400, message = "Error")

@ApiApp.route('/api/v1/admin/timer/remove/<player>', methods=['POST'])
def admin_removeTime(player):
    try: 
        response = ControllerEvent().admin_removeTime(player)
        return jsonify(status=200)
    except:
        return jsonify(status=400, message = "Error")

@ApiApp.route('/api/v1/admin/timer/on/<player>', methods=['POST'])
def admin_playerIsPlaying(player):
    try: 
        response = ControllerEvent().admin_changeStatusPlayer(player, True)
        return jsonify(status=200)
    except:
        return jsonify(status=400, message = "Error")
    
@ApiApp.route('/api/v1/admin/timer/off/<player>', methods=['POST'])
def admin_playerIsNotPlaying(player):
    try: 
        response = ControllerEvent().admin_changeStatusPlayer(player, False)
        return jsonify(status=200)
    except:
        return jsonify(status=400, message = "Error")

@ApiApp.route('/api/v1/admin/reset', methods=['POST'])
def admin_reset():
    try: 
        ControllerEvent().admin_changeStatus('PAUSE')
        response = ControllerEvent().admin_reset()
        return jsonify(status=200)
    except:
        return jsonify(status=400, message = "Error")

@ApiApp.route('/api/v1/public/<id>/time/use/<player>', methods=['POST'])
def public_useTime(id,player):
    try: 
        ControllerEvent().public_useTime(int(id),player)
        return jsonify(status=200)
    except:
        return jsonify(status=400, message = "Error")

# @ApiApp.route('/api/v1/public/<ip>', methods=['POST'])
# def create_public(ip):
#     print("Create")
#     try: 
#         ControllerEvent().public_create(ip)
#         return jsonify(status=200,)
#     except Exception:
#         print(Exception)
#         return jsonify(status=400, message = "Error")

@ApiApp.route('/api/v1/public/', methods=['POST'])
def create_public():
    try: 
        public_id = ControllerEvent().public_create("t")
        if(public_id>=0):
            return jsonify(status=200, id = public_id)
        else:
            return jsonify(status=503, message = "Error")
    except Exception:
        print(Exception)
        return jsonify(status=400, message = "Error")


# GET API ======================================================================

@ApiApp.route('/api/v1/public', methods=['GET'])
def get_Publics():
    try: 
        response = ControllerModel().get_Publics().toJSON()
        return jsonify(status=200, response = response)
    except:
        return jsonify(status=400, message = "Error")

@ApiApp.route('/api/v1/public/<id>', methods=['GET'])
def get_Public(id):
    try: 
        response = ControllerModel().get_Public(int(id)).toJSON()
        return jsonify(status=200, response = response)
    except:
        return jsonify(status=400, message = "Error")

@ApiApp.route('/api/v1/player', methods=['GET'])
def get_PlayerList():
    try: 
        response = ControllerModel().get_PlayerList().toJSON()
        return jsonify(status=200, response = response)
    except:
        return jsonify(status=400, message = "Error")


@ApiApp.route('/api/v1/admin/publicsize', methods=['GET'])
def admin_size():
    try: 
        response = ControllerModel().get_PublicSize()
        return jsonify(status=200, response = response)
    except:
        return jsonify(status=400, message = "Errora")
