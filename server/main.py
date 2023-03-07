if __name__ == '__main__':

    print("Shop Link Server")
    print("----------------")
    print("")

    print("Initialize")
    from database import db
    from server import app

    print("Run")
    app.run(debug=True, use_reloader=False, port=80, threaded=True)

    print("Quit")
    db.close()

    print("Exit")
