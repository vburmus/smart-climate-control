import React, {useState} from 'react';
import Loader from "../components/common/Loader";
import AlertRowComponent from "../components/AlertRowComponent";
const AlertsPage = () => {
    const alertParams = [
        "Action", "Cause", "Room", "Date", "Time"
    ];
    const [isLoading, setIsLoading] = useState(false)

    return (isLoading ? <Loader/> :
            <div className="d-flex flex-column m-5 gap-3 w-75">
                <h1 className="fw-bold text-primary text-center">Your alerts:</h1>

                <table style={{ borderRadius: '20px', overflow: 'hidden' }}>
                    <thead className="bg-primary">
                        <tr className="border-bottom border-top-0 border-end-0 border-start-0 border-3 border-primary">
                            {alertParams.map((cat) => {
                                return <th className="fw-bold text-white fs-3 text-center rounded-top-3 p-3">{cat}</th>
                            })}
                        </tr>
                    </thead>
                    <tbody>
                        <AlertRowComponent/>
                    </tbody>

                </table>
            </div>
    );
};

export default AlertsPage;