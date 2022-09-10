from Libs.Controller.controllerEvent import ControllerEvent
from flask import Flask, jsonify, request

from Libs.Controller.controllerModel import ControllerModel
 
ApiApp = Flask(__name__)
ApiDbg=True
ApiPort=5000
ApiHost='0.0.0.0'

# STD API ROUT ==================================================================
@ApiApp.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@ApiApp.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

# POST API ======================================================================

@ApiApp.route('/api/v1/admin/<status>', methods=['POST'])
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

@ApiApp.route('/api/v1/admin/timer/start/<player>', methods=['POST'])
def admin_startTimer(player):
    try: 
        response = ControllerEvent().admin_toogleTimer(player)
        return jsonify(status=200)
    except:
        return jsonify(status=400, message = "Error")

@ApiApp.route('/api/v1/admin/reset', methods=['POST'])
def admin_reset():
    try: 
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
    print("Create")
    try: 
        public_id = ControllerEvent().public_create("t")
        return jsonify(status=200, id = public_id)
    except Exception:
        print(Exception)
        return jsonify(status=400, message = "Error")


# GET API ======================================================================

@ApiApp.route('/api/v1/public', methods=['GET'])
def get_Publics():
    try: 
        print("test")
        response = ControllerModel().get_Publics().toJSON()
        print(response)
        return jsonify(status=200, response = response)
    except:
        return jsonify(status=400, message = "Error")

@ApiApp.route('/api/v1/public/<id>', methods=['GET'])
def get_Public(id):
    try: 
        print("test")
        response = ControllerModel().get_Public(int(id)).toJSON()
        print(response)
        return jsonify(status=200, response = response)
    except:
        return jsonify(status=400, message = "Error")

@ApiApp.route('/api/v1/player', methods=['GET'])
def get_PlayerList():
    try: 
        response = ControllerModel().get_PlayerList().toJSON()
        print(response)
        return jsonify(status=200, response = response)
    except:
        return jsonify(status=400, message = "Error")

if __name__ == '__main__':
    ApiApp.run(host=ApiHost, port=ApiPort, debug=ApiDbg)