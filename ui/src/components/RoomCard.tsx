import React from 'react';
import {DropletFill, Speedometer, Thermometer} from "react-bootstrap-icons";
import {Room} from "../utils/types";
import {Link} from "react-router-dom";
import "../styles/Hover.css"

type RoomCardProps = {
    room: Room
}

const RoomCard = ({room}: RoomCardProps) => {
    return (
        <Link to={`/room/${room.id}`} style={{ textDecoration: 'none' }}>
            <div className="d-flex flex-column bg-primary rounded-4 hover-class">
                <div className="p-2">
                    <h3 className="fw-bold text-white text-center">Room #{room.id}</h3>
                </div>
                <div className="bg-info rounded-bottom-4 px-3 py-3">
                    <p className="fw-bold text-center text-black fs-4">Last Update</p>
                    <div className="d-flex flex-wrap mt-5 gap-4">
                        <div className="d-flex flex-column gap-3 align-items-center justify-content-center px-4">
                            <Thermometer size={35} className="text-black"/>
                            <p className="fw-bold text-center text-black fs-5">{room.temperature} °C</p>
                        </div>
                        <div className="d-flex flex-column gap-3 align-items-center justify-content-center px-4">
                            <DropletFill size={35} className="text-black"/>
                            <p className="fw-bold text-center text-black fs-5">{room.humidity} %</p>
                        </div>
                        <div className="d-flex flex-column gap-3 align-items-center justify-content-center px-4">
                            <Speedometer size={35} className="text-black"/>
                            <p className="fw-bold text-center text-black fs-5">{room.pressure} hPa</p>
                        </div>
                    </div>
                </div>
            </div>
        </Link>
    );
};

export default RoomCard;