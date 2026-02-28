import streamlit as st
import pydeck as pdk
import polyline
from app.core.planner import plan_route
from app.traffic.simulator import RouteSimulator
from app.services.google_service import geocode_place
from app.traffic.rerouter import intelligent_reroute
st.set_page_config(layout="wide")
st.title("🚗 Smart Traffic & Parking Optimizer")
st.sidebar.header("Route Settings")
origin_name = st.sidebar.text_input("Origin", "Mumbai")
destination_name = st.sidebar.text_input("Destination", "Pune")
use_parking = st.sidebar.checkbox("Use Parking Optimization")
plan_button = st.sidebar.button("Plan Route")
if plan_button:
    origin = geocode_place(origin_name)
    destination = geocode_place(destination_name)
    if not origin or not destination:
        st.error("Invalid location name")
        st.stop()
    result = plan_route(origin, destination, use_parking=use_parking)
    if not result:
        st.error("No route found.")
    else:
        if use_parking:
            route = result["route"]
            st.success("Parking Optimized Route Selected")

            total_time = result["drive_time"] + result["walking_time"]

            st.write("### Trip Summary")
            st.write("Total Travel Time (min):", round(total_time / 60))
            st.write("Drive Time (min):", round(result["drive_time"] / 60))
            st.write("Walking Time (min):", round(result["walking_time"] / 60))
            st.write("Parking Cost:", result["cost"])
            st.write("Parking Spots Available:", result["available_spots"])
        else:
            route = result
            st.success("Traffic Optimized Route Selected")
            st.write("Traffic Duration:", route["traffic_duration"])
        decoded = polyline.decode(route["polyline"])
        layer = pdk.Layer(
            "PathLayer",
            data=[{"path": decoded}],
            get_path="path",
            get_width=5,
            width_scale=1,
            width_min_pixels=4,
            get_color=[0, 0, 255],
        )
        mid_lat = (decoded[0][0] + decoded[-1][0]) / 2
        mid_lng = (decoded[0][1] + decoded[-1][1]) / 2

        view_state = pdk.ViewState(
            latitude=mid_lat,
            longitude=mid_lng,
            zoom=9,
            pitch=0,
        )
        r = pdk.Deck(
            map_style="road",
            layers=[layer],
            initial_view_state=view_state,
        )
        st.pydeck_chart(r)