from App.application import Application
from App._Game.settings import RUN_CONFIG


if __name__ == "__main__":
    app = Application(RUN_CONFIG)
    app.run()
