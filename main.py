import cairosvg

# CONSTANTS
TOTAL_EVENTS_NUM = 10585
TOTAL_CASES_NUM = 666


# FUNCTIONS
def convert_svg_to_png(svg_file_path, png_file_path, scale=1.0):
    # Read the SVG content
    with open(svg_file_path, 'r') as svg_file:
        svg_content = svg_file.read()

    # Convert SVG to PNG with high quality
    cairosvg.svg2png(
        bytestring=svg_content.encode('utf-8'),
        write_to=png_file_path,
        scale=scale,
        background_color='white'
    )


def print_log_info(log_df, total_events_num=None, total_cases_num=None):
    num_events = len(log_df)
    num_cases = len(log_df['case:concept:name'].unique())

    if total_events_num and total_cases_num:
        events_percentage = (num_events / total_events_num) * 100
        cases_percentage = (num_cases / total_cases_num) * 100
    else:
        events_percentage, cases_percentage = (100, 100)

    print("Number of events: {} ({:.2f}%)".format(num_events, events_percentage))
    print("Number of cases: {} ({:.2f}%)".format(num_cases, cases_percentage))
    print('\n')

    return num_events, num_cases


# USAGE

# Example usage
svg_file_path = 'charts\\horizon_chart_PMTK.svg'  # Replace with your SVG file path
png_file_path = 'charts\\horizon_chart_PMTK.png'  # Replace with your desired output PNG file path

convert_svg_to_png(svg_file_path, png_file_path, scale=2.0)
