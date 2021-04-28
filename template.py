import os


dirs = [
    os.path.join("data", "raw"),                # To store raw data
    os.path.join("data", "processed"),          # To store processed data
    os.path.join("data_given", "processed"),    # To store processed data
    "notebooks",                                # To store notebooks which we can use to verify facts/tasks
    "saved_models",                             # To store models after trial n error
    "src",                                      # Source folder where we can store py files: model, preprocessing ,evaluation
    "report",                                   # Used to store parameters and matrics(scores)
    "prediction_service",                       # Used in case of MLFlow
    "tests",                                    # Used to store Unit test
    os.path.join("webapp", "static","css") ,    # Used to store UI-css code
    os.path.join("webapp", "static","Script"),  # Used to store UI-scrips code
    os.path.join("webapp", "templates")         # Used to store UI-webpage templates

]
for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, '.gitkeep'), "w") as f:
        pass


files = [
    "dvc.yaml",                                         #DVC congiguration file where all command to be run on dvc are kept
    "params.yaml",                                      #congiguratioon file where all parametrs and configurations are kept
    "app.py"                                            #Flask app file starting point of project
    ".gitingnore",
    os.path.join("src", "__init__.py"),
    os.path.join("prediction_service", "__init__.py"),
    os.path.join("tests", "__init__.py")

]
for file_ in files:
    with open(file_, "w") as f:
        pass
