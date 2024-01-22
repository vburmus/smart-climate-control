import React from 'react';
import {DropletFill, Thermometer} from "react-bootstrap-icons";
import {Room} from "../utils/types";

type RoomCardProps = {
    room: Room
}

const RoomCard = ({room}: RoomCardProps) => {
    return (
        <div className="d-flex flex-column bg-primary rounded-4">
            <div className="p-3">
                <h2 className="fw-bold text-white text-center">Room #{room.id}</h2>
            </div>
            <div className="bg-info p-4 rounded-bottom-4 px-5">
                <h4 className="fw-bold text-center">Last Update</h4>
                <div className="d-flex flex-wrap mt-5 gap-4">
                    <div className="d-flex flex-column gap-3 align-items-center px-4">
                        <Thermometer size={35}/>
                        <h5 className="fw-bold text-center">{room.temperature} °C</h5>
                    </div>
                    <div className="d-flex flex-column gap-3 align-items-center px-4">
                        <DropletFill size={35}/>
                        <h5 className="fw-bold text-center">{room.humidity} %</h5>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default RoomCard;