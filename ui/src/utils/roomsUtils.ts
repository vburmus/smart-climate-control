import axiosInstance from "./axiosConfig";
import {UpdateRequest} from "./types";

const roomsEndpoint = "/api/v1/rooms";
const findAllRooms = async () => {
    const response = await axiosInstance.get(roomsEndpoint)
    return response.data
}

const findRoom = async (id: string) => {
    const response = await axiosInstance.get(roomsEndpoint + `/${id}`)
    return response.data
}

const updatePreferredTemperature = async (id:string, updateRequest: UpdateRequest) => {
    const response = await axiosInstance.post(roomsEndpoint + `/update-temperature/${id}`, updateRequest)
    return response.data
}

export {findAllRooms, findRoom, updatePreferredTemperature}