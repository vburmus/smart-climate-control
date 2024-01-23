import React from 'react';
import {Room} from "../utils/types";
import {DropletFill} from "react-bootstrap-icons";
import {Image} from "react-bootstrap";

type HumidityComponentProps = {
    room?: Room,
    plot?: string
}

const HumidityComponent = ({room, plot}: HumidityComponentProps) => {
    return (
        <div className="d-flex justify-content-between align-items-center w-100">
            <div className="d-flex flex-column bg-primary rounded-4 hover-class">
                <div className="p-3">
                    <h2 className="fw-bold text-white text-center">Humidity</h2>
                </div>
                <div className="bg-info p-4 rounded-bottom-4 p-5">
                    <h4 className="fw-bold text-center text-black">Last
                        Update: {room?.time && new Date(room.time).toLocaleTimeString()}</h4>
                    <div className="d-flex flex-column flex-wrap mt-5 gap-4">
                        <div className="d-flex gap-3 align-items-center justify-content-between px-4">
                            <h5 className="fw-bold text-center text-black">Actual:</h5>
                            <h5 className="fw-bold text-center text-black">{room?.humidity} %</h5>
                            <DropletFill size={35} className="text-black"/>
                        </div>
                    </div>
                </div>
            </div>
            <div>
                <Image src={`data:image/png;base64, ${plot}`}/>
            </div>
        </div>
    );
};

export default HumidityComponent;