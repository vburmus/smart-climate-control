import React, {useState} from 'react';
import {Thermometer} from "react-bootstrap-icons";
import {Button, Image} from "react-bootstrap";
import {Room} from "../utils/types";
import ChangeTemperatureModal from "./modals/ChangeTemperatureModal";

type TemperatureComponentProps = {
    room?: Room,
    plot?: string,
    setIsLoading: (state:boolean) => void
}

const TemperatureComponent = ({room, plot, setIsLoading}: TemperatureComponentProps) => {
    const [isModalOpened, setIsModalOpened] = useState(false)

    return (
        <div className="d-flex justify-content-between align-items-center w-100">
            <div className="d-flex flex-column bg-primary rounded-4 hover-class">
                <div className="p-2">
                    <p className="fw-bold text-white text-center fs-3">Temperature</p>
                </div>
                <div className="bg-info p-4 rounded-bottom-4 p-3">
                    <p className="fw-bold text-center text-black fs-4">Last
                        Update: {room?.time && new Date(room.time).toLocaleTimeString()}</p>
                    <div className="d-flex flex-column flex-wrap mt-5 gap-4">
                        <div className="d-flex gap-3 align-items-center justify-content-between px-4">
                            <p className="fw-bold text-center text-black fs-5">Actual:</p>
                            <p className="fw-bold text-center text-black fs-5">{room?.temperature} °C</p>
                            <Thermometer size={35} className="text-black"/>
                        </div>
                        <div className="d-flex gap-3 align-items-center justify-content-between px-4">
                            <p className="fw-bold text-center text-black fs-5">Preferred:</p>
                            <p className="fw-bold text-center text-black fs-5">{room?.preferred_temp} °C</p>
                            <Thermometer size={35} className="text-black"/>
                        </div>
                        <Button onClick={() => setIsModalOpened(true)} className="rounded-3 fw-bold">Change preferred temperature</Button>
                        <ChangeTemperatureModal isModalOpened={isModalOpened} setIsModalOpened={setIsModalOpened} setIsLoading={setIsLoading} roomId={room?.id}/>
                    </div>
                </div>
            </div>
            <div>
                <Image src={`data:image/png;base64, ${plot}`} style={{width: 900}}/>
            </div>
        </div>
    );
};

export default TemperatureComponent;