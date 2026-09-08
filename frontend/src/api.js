import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const getClimateData = () => {
    return axios.get(`${API_URL}/api/climate-data/`);
};

export const getWeatherStations = () => {
    return axios.get(`${API_URL}/api/weather-stations/`);
};
