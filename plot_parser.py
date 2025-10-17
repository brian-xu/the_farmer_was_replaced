VERTICAL = -1
HORIZONTAL = -2

# plot list structure
# [[crop, plot_id]...]
# {plot_id: [top, left, height, width]}


def hstack(plots):
    stack = []
    for plot in plots:
        stack.append(plot)
    stack.append(HORIZONTAL)
    return stack


def vstack(plots):
    stack = []
    for plot in plots:
        stack.append(plot)
    stack.append(VERTICAL)
    return stack


def parse_recursive(block, root=False):
    global plot_count
    parsed = []
    plots = {}
    if root:
        plot_count = 0
    if block[-1] == VERTICAL:
        parsed, plots = parse_recursive(block[0])
        height = len(parsed)
        width = len(parsed[0])
        for sub in block[1:-1]:
            sub_parsed, sub_plots = parse_recursive(sub)
            for row in sub_parsed:
                parsed.append(row)
            for plot in sub_plots:
                top, left, h, w = sub_plots[plot]
                plots[plot] = [top + height, left, h, w]
            height += len(sub_parsed)
    elif block[-1] == HORIZONTAL:
        parsed, plots = parse_recursive(block[0])
        height = len(parsed)
        width = len(parsed[0])
        for sub in block[1:-1]:
            i = 0
            sub_parsed, sub_plots = parse_recursive(sub)
            for row in sub_parsed:
                parsed[i] = parsed[i] + row
                i += 1
            for plot in sub_plots:
                top, left, h, w = sub_plots[plot]
                plots[plot] = [top, left + width, h, w]
            width += len(sub_parsed[0])
    else:
        crop = block[0]
        height = block[1]
        width = block[2]
        row = []
        for j in range(width):
            row.append([crop, plot_count])
        for i in range(height):
            parsed.append(row)
        plots[plot_count] = [0, 0, height, width]
        plot_count += 1
        if plot_count > 31:
            quick_print("subplots exceeded limit!")
            x = 5 / 0
    return parsed, plots
