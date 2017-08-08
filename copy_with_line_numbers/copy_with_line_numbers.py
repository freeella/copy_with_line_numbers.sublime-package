import sublime, sublime_plugin
import os


def get_line_num(obj, point):
    return obj.view.rowcol(point)[0] + 1


def create_output_body(obj, output):
    
    sels = obj.view.sel()

    # To print all the line numbers with the same length
    max_line_num = get_line_num(obj, sels[-1].end())
    max_line_num_len = len(str(max_line_num))
    format_string = "%0" + str(max_line_num_len) + "d: %s\n"

    # handle text
    isFollowupSelection = None
    for selection in sels:
        if isFollowupSelection:
            # split multi selections with ---
            output += "---\n"
        else:
            # but not the first one
            isFollowupSelection = True
        # for each selection
        selection = obj.view.line(selection)  # Extend selection to full lines
        first_line_num = get_line_num(obj, selection.begin())
        lines = obj.view.substr(selection).split("\n")  # Considers all line breaks
        for i, line in enumerate(lines):
            output += format_string % (first_line_num + i, line)

    return output


# command: "copy_with_line_numbers_text"
class CopyWithLineNumbersTextCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = sublime.Window.active_view(sublime.active_window())

        # header - set file name
        if view.file_name():
        	output = "File: " + view.file_name() + "\n"
        else:
        	output = "File: <unsaved>\n"

        # body
        output = create_output_body(self, output)

        # send to clipboard
        sublime.set_clipboard(output)


# command: "copy_with_line_numbers_jira"
class CopyWithLineNumbersJiraCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = sublime.Window.active_view(sublime.active_window())

        # header - set file name
        if view.file_name():
            # Need to replace DOS path \ with /
            output = "{code:java|titleBGColor=#F7D6C1|title=File: " + view.file_name().replace("\\","&#92;" ) + "}\n"
        else:
            output = "{code:java|titleBGColor=#F7D6C1|title=File: <unsaved>}\n"

        # body
        output = create_output_body(self, output)

        # Footer
        output += '{code}'

        # send to clipboard
        sublime.set_clipboard(output)

