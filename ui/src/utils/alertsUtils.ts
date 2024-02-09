import axiosInstance from "./axiosConfig";

const alertsEndpoint = "/api/v1/alerts";
const findAllAlerts = async () => {
    const response = await axiosInstance.get(alertsEndpoint)
    return response.data
}

export {findAllAlerts}