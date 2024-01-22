import axiosInstance from "./axiosConfig";

const roomsEndpoint = "/api/v1/rooms";
const findAllRooms = async () => {
    const response = await axiosInstance.get(roomsEndpoint)
    return response.data
}

export {findAllRooms}