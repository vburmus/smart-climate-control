import axiosInstance from "./axiosConfig";

const plotsEndpoint = "/api/v1/rooms/plot";

const findPlots = async (id: string) => {
    const response = await axiosInstance.get(plotsEndpoint + `/${id}`)
    return response.data
}

export {findPlots}