import axios from "axios";

const apiBaseURL = "http://localhost:8000/api/"

const api = axios.create({
  baseURL: apiBaseURL,
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access_token");
  if (token) {
    config.headers["Authorization"] = `Bearer ${token}`;
  }
  return config;
});


export const apiWithoutToken = axios.create({
  baseURL: apiBaseURL,
});


export default api;