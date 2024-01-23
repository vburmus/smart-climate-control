import axiosInstance from "./axiosConfig";

const roomsEndpoint = "/api/v1/rooms";
const findAllRooms = async () => {
    const response = await axiosInstance.get(roomsEndpoint)
    return response.data
}

const findRoom = async (id: string) => {
    const response = await axiosInstance.get(roomsEndpoint + `/${id}`)
    return response.data
}

export {findAllRooms, findRoom}