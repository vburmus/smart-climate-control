import React from 'react';
import Loader from "../components/common/Loader";
import {Image} from "react-bootstrap";
import "../styles/Hover.css"

const HomePage = () => {
    return (
        <div className="d-flex flex-column m-5 gap-5 align-items-center">
            <h1 className="fw-bold text-primary text-center">Smart Climate Control</h1>
            <div className="w-50">
                <h4 className="fw-bold text-center">
                    Welcome to Smart Climate Control,
                    your personalized solution for maintaining a comfortable and secure environment in your home.
                    Our application utilizes a network of Raspberry Pi devices to monitor and manage the climate conditions of each room,
                    ensuring that you have full control over temperature and humidity levels.
                    With encrypted MQTT communication via Mosquitto,
                    data is securely transmitted from client Raspberry Pi devices equipped with sensors to the central server Raspberry Pi.
                    This information is then stored in a database,
                    allowing you to access and track real-time and historical data through our user-friendly web application.
                    Take charge of your home's climate with Smart Climate Control.
                </h4>
            </div>

            <div className="d-flex flex-wrap align-items-center w-100 justify-content-around">
                <div className="d-flex flex-column gap-5 w-50 hover-class">
                    <h1 className="fw-bold text-primary text-center">Sensors in your house?</h1>
                    <h4 className="fw-bold text-center">Smart Climate Control empowers you with a comprehensive sensor network strategically placed in each room of your house.
                        These sensors, integrated into client Raspberry Pi devices, continuously measure temperature and humidity.
                        The gathered data is transmitted securely to the central server,
                        providing you with accurate and up-to-date information about the climate conditions in every corner of your home.
                    </h4>
                </div>
                <Image src="https://image.lexica.art/full_webp/24f038eb-143d-4c80-9c81-d27e1059ef59" style={{width: 500, height:400, borderRadius: 50}} className="hover-class"/>
            </div>

            <div className="d-flex flex-wrap align-items-center w-100 justify-content-around">
                <Image src="https://image.lexica.art/full_webp/1f087e37-2bda-4a1d-8141-b1f92526e360" style={{width: 500, height:400, borderRadius: 50}} className="hover-class"/>
                <div className="d-flex flex-column gap-5 w-50 hover-class">
                    <h1 className="fw-bold text-primary text-center">Check the room situation!</h1>
                    <h4 className="fw-bold text-center">Curious about the current climate in a specific room?
                        Our web application enables you to effortlessly check the situation in each room equipped with Smart Climate Control.
                        Explore real-time temperature and humidity data,
                        ensuring that you are always aware of the comfort levels throughout your home.
                        Stay informed and make informed decisions to create the perfect atmosphere in every room.
                    </h4>
                </div>
            </div>

            <div className="d-flex flex-wrap align-items-center w-100 justify-content-around">
                <div className="d-flex flex-column gap-5 w-50 hover-class">
                    <h1 className="fw-bold text-primary text-center">Add room to application!</h1>
                    <h4 className="fw-bold text-center">Customize Smart Climate Control to match the unique layout of your home by easily adding rooms to the application.
                        Simply configure a client Raspberry Pi in the desired room, and our system will seamlessly integrate it into the network.
                        Once added, you can monitor and control the climate conditions in the new room through the intuitive web interface, ensuring a tailored and comfortable environment.
                    </h4>
                </div>
                <Image src="https://image.lexica.art/full_webp/2b9277fd-fe87-4011-8b7a-01b7605bbc11" style={{width: 500, height:400, borderRadius: 50}} className="hover-class"/>
            </div>

            <div className="d-flex flex-wrap align-items-center w-100 justify-content-around">
                <Image src="https://image.lexica.art/full_webp/4994521b-772c-461d-bbaf-bbf55f44cc8e" style={{width: 500, height:400, borderRadius: 50}} className="hover-class"/>
                <div className="d-flex flex-column gap-5 w-50 hover-class">
                    <h1 className="fw-bold text-primary text-center">Receive alerts!</h1>
                    <h4 className="fw-bold text-center">Stay connected and informed with Smart Climate Control's alert system.
                        Receive instant notifications on your web app for critical events such as smoke detection or unusually low temperatures.
                        Take swift action with confidence, whether it's calling firefighters in case of smoke detection or adjusting the temperature settings to address low temperatures.
                        Keep track of all alerts in the web application, ensuring a proactive approach to maintaining a safe and comfortable home environment.
                        Smart Climate Control puts you in control, providing peace of mind for your household.
                    </h4>
                </div>
            </div>

        </div>
    );
};

export default HomePage;