import React, {useEffect, useState} from 'react';
import Loader from "../components/common/Loader";
import RoomCard from "../components/RoomCard";
import {findAllRooms} from "../utils/roomsUtils";
import {Room} from "../utils/types";
import {isAxiosError} from "axios";

const RoomsPage = () => {
    const [isLoading, setIsLoading] = useState(true)
    const [rooms, setRooms] = useState<Room[]>()
    const [error, setError] = useState("")

    const fetchData = async () => {
        try {
            const result = await findAllRooms();
            setRooms(result.rooms)
        } catch(e) {
            if (isAxiosError(e) && e.response) {
                setError(e.response.data.message)
            }
        } finally {
            setIsLoading(false);
        }
    };


    useEffect(() => {
        fetchData()
    }, []);


    return ( isLoading ? <Loader/> : error || !rooms ? <h1 className="m-5 fw-bold text-center text-danger">{error}</h1> :
        <div className="d-flex flex-column m-5 gap-5">
            <h1 className="fw-bold text-primary text-center">Your rooms:</h1>
            <div className="d-flex flex-wrap gap-5 justify-content-center">
                {rooms.map((room) => {
                    return <RoomCard room={room}/>
                })}
            </div>
        </div>
    );
};

export default RoomsPage;