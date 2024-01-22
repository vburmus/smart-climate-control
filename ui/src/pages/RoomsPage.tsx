import React, {useState} from 'react';
import Loader from "../components/common/Loader";
import RoomCard from "../components/RoomCard";

const RoomsPage = () => {
    const [isLoading, setIsLoading] = useState(false)

    return ( isLoading ? <Loader/> :
        <div className="d-flex flex-column m-5 gap-5">
            <h1 className="fw-bold text-primary text-center">Your rooms:</h1>
            <div className="d-flex flex-wrap gap-5 justify-content-center">
                <RoomCard/>
            </div>
        </div>
    );
};

export default RoomsPage;