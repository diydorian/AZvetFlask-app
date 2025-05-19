from flask import Flask, render_template_string
import folium

app = Flask(__name__)

@app.route('/')
def hello_veterans():
    # Create a map centered on Arizona
    m = folium.Map(location=[34.0489, -111.0937], zoom_start=7)
    
    # Add a marker for Phoenix
    folium.Marker(
        [33.4484, -112.0740],
        popup="Phoenix",
        tooltip="State Capital"
    ).add_to(m)
    
    # Add a marker for the Northern Arizona VA Health Care System in Prescott
    folium.Marker(
        [34.5550, -112.4717],
        popup="""
        <b>Northern Arizona VA Health Care System</b><br>
        500 N. Highway 89, Prescott, AZ 86313<br>
        Main Phone: (928) 445-4860<br>
        Mental Health: (928) 445-4860 ext. 6600<br>
        <a href="https://www.va.gov/northern-arizona-health-care/" target="_blank">Website</a>
        """,
        tooltip="Prescott Veterans Hospital",
        icon=folium.Icon(color='red', icon='plus-sign')
    ).add_to(m)
    
    # Get the HTML representation of the map
    map_html = m._repr_html_()
    
    # Create an HTML template with the greeting, map, and additional information
    html = f"""
    <h1>Hello, Arizona Veterans!</h1>
    <p>The map below shows the location of the Northern Arizona VA Health Care System in Prescott.</p>
    {map_html}
    <h2>Public Transportation</h2>
    <p>The Yavapai Regional Transit provides bus service to the VA Medical Center:</p>
    <ul>
        <li>Route 1: Chino Valley to Prescott</li>
        <li>Route 2: Prescott to Prescott Valley</li>
    </ul>
    <p>For more information, visit <a href="https://www.yavapairegionaltransit.com/" target="_blank">Yavapai Regional Transit</a> or call (928) 636-3602.</p>
    <h2>Contact Information</h2>
    <ul>
        <li>Main Phone: (928) 445-4860</li>
        <li>Mental Health: (928) 445-4860 ext. 6600</li>
        <li>Veterans Crisis Line: 1-800-273-8255 (Press 1)</li>
    </ul>
    """
    
        # Modify the HTML template to include a container and adjust the map size
    html = f"""
    <style>
        .container {{ max-width: 800px; margin: 0 auto; padding: 20px; }}
        .map-container {{ height: 400px; }}
    </style>
    <div class="container">
        <h1>Hello, Arizona Veterans!</h1>
        <p>The map below shows the location of the Northern Arizona VA Health Care System in Prescott.</p>
        <div class="map-container">
            {map_html}
        </div>
        <h2>Public Transportation</h2>
        <p>The Yavapai Regional Transit provides bus service to the VA Medical Center:</p>
        <ul>
            <li>Route 1: Chino Valley to Prescott</li>
            <li>Route 2: Prescott to Prescott Valley</li>
        </ul>
        <p>For more information, visit <a href="https://www.yavapairegionaltransit.com/" target="_blank">Yavapai Regional Transit</a> or call (928) 636-3602.</p>
        <h2>Contact Information</h2>
        <ul>
            <li>Main Phone: (928) 445-4860</li>
            <li>Mental Health: (928) 445-4860 ext. 6600</li>
            <li>Veterans Crisis Line: 1-800-273-8255 (Press 1)</li>
        </ul>
    </div>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)