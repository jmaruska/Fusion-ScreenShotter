import adsk.core, adsk.fusion, adsk.cam, traceback

# Define global variables for the application and user interface
global app, ui
app = adsk.core.Application.get()
ui = app.userInterface

# Button definition properties
buttonProps = {
    'id': 'jm_ScreenShotterCommand',
    'displayName': 'Screen Capture',
    'description': 'Launch the screen capture tool via a key binding.',
    'resources': 'resources'
}

# Maintain a global list to keep all event handlers in scope
handlers = []

class CommandCreatedEventHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        # Handle the command created event
        eventArgs = adsk.core.CommandCreatedEventArgs.cast(args)
        cmd = eventArgs.command

        # Connect to the execute event
        onExecute = CommandExecuteHandler()
        cmd.execute.add(onExecute)
        handlers.append(onExecute)  # Keep the handler in scope

class CommandExecuteHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        # Execute the "Capture Image…" command if available
        saveAsImageCmdDef = ui.commandDefinitions.itemById('SaveAsImageCommand')
        if saveAsImageCmdDef:
            saveAsImageCmdDef.execute()
        else:
            ui.messageBox('Capture Image command not found.')

def run(context):
    try:
        # Create a button command definition using properties from the dictionary
        toolbarButton = ui.commandDefinitions.addButtonDefinition(
            buttonProps['id'],
            buttonProps['displayName'],
            buttonProps['description'],
            buttonProps['resources']
        )

        # Connect to the command created event
        commandCreated = CommandCreatedEventHandler()
        toolbarButton.commandCreated.add(commandCreated)
        handlers.append(commandCreated)

        # Add the button to the ADD-INS panel in the model workspace
        addInsPanel = ui.allToolbarPanels.itemById('SolidScriptsAddinsPanel')
        buttonControl = addInsPanel.controls.addCommand(toolbarButton)

        # Promote the button in the panel by default
        if buttonControl:
            buttonControl.isPromotedByDefault = True
            buttonControl.isPromoted = True
    except:
        ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    try:
        # Remove the custom button and its command definition
        cmdDef = ui.commandDefinitions.itemById(buttonProps['id'])
        if cmdDef:
            cmdDef.deleteMe()

        addinsPanel = ui.allToolbarPanels.itemById('SolidScriptsAddinsPanel')
        control = addinsPanel.controls.itemById(buttonProps['id'])
        if control:
            control.deleteMe()
    except:
        ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
