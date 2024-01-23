import React, {useEffect, useState} from 'react';
import {Link, useParams} from "react-router-dom";
import {findRoom} from "../utils/roomsUtils";
import {isAxiosError} from "axios";
import Loader from "../components/common/Loader";
import {Plots, Room} from "../utils/types";
import {findPlots} from "../utils/plotsUtils";
import {Button} from "react-bootstrap";
import {ArrowLeft} from "react-bootstrap-icons";
import "../styles/Hover.css"
import TemperatureComponent from "../components/TemperatureComponent";
import HumidityComponent from "../components/HumidityComponent";
import PressureComponent from "../components/PressureComponent";

const RoomDetailsPage = () => {
    const {id} = useParams()
    const [room, setRoom] = useState<Room>()
    const [error, setError] = useState("")
    const [isLoading, setIsLoading] = useState(true)
    const [plots, setPlots] = useState<Plots>()

    const fetchData = async () => {
        if (id) {
            try {
                const room = await findRoom(id);
                const plots = await findPlots(id);
                setPlots(plots)
                setRoom(room)
                console.log(room)
            } catch (e) {
                if (isAxiosError(e) && e.response) {
                    setError(e.response.data.message)
                }
            } finally {
                setIsLoading(false)
            }
        } else {
            setError("Wrong params provided!")
        }
    };

    useEffect(() => {
        fetchData()
    }, []);

    return (isLoading ? <Loader/> : error ? <h1 className="m-5 fw-bold text-center text-danger">{error}</h1> :
            <div className="d-flex flex-column m-5">
                <h1 className="fw-bold text-primary text-center">Room #{id} ({room?.name})</h1>
                <div>
                    <Link to={`/rooms`}>
                        <Button variant="primary" className="rounded-3 fw-bold text-white fs-5 px-5 py-3">
                            <ArrowLeft size={25}/> Back
                        </Button>
                    </Link>
                </div>
                <TemperatureComponent room={room} plot={plots?.temperature}/>
                <HumidityComponent room={room} plot={plots?.humidity}/>
                <PressureComponent room={room} plot={plots?.pressure}/>
            </div>
    );
};

export default RoomDetailsPage;