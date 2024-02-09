import React, {useState} from 'react';
import {Button, Modal} from "react-bootstrap";
import {Input} from "reactstrap";
import {UpdateRequest} from "../../utils/types";
import {updatePreferredTemperature} from "../../utils/roomsUtils";
import {isAxiosError} from "axios";

type TemperatureModalProps = {
    isModalOpened: boolean,
    setIsModalOpened: (state: boolean) => void,
    setIsLoading: (state: boolean) => void,
    roomId?: number
}

const ChangeTemperatureModal = ({isModalOpened, setIsModalOpened, setIsLoading, roomId}: TemperatureModalProps) => {
    const [providedTemperature, setProvidedTemperature] = useState("")
    const [error, setError] = useState("")

    const handleCloseModal = () => {
        setError("")
        setIsModalOpened(false)
    }

    const handleTemperatureEntered = () => {
        setError("")
        if (isFloat(providedTemperature)) {
            setIsModalOpened(false)
            setError("")
            setIsLoading(true)
            updateData()
        } else {
            setError("Enter valid number!")
        }
    }

    const updateData = async () => {
        if (roomId) {
            try {
                const updateRequest: UpdateRequest = {
                    preferred_temp: parseFloat(providedTemperature)
                }
                const result = await updatePreferredTemperature(roomId.toString(), updateRequest);
                console.log(result)
            } catch (e) {
                if (isAxiosError(e) && e.response) {
                    setError(e.response.data.message)
                }
            } finally {
                window.location.reload()
            }
        }
    }

    function isFloat(str: string): boolean {
        const number = parseFloat(str);
        return !isNaN(number);
    }

    return (
        <Modal show={isModalOpened} onHide={handleCloseModal} backdrop="static" centered>
            <Modal.Header closeButton>
                <Modal.Title className="ms-auto">Provide preferred temperature:</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Input
                    className={error === "" ? `rounded-3` : `rounded-3 border border-danger border-2`}
                    placeholder="Temperature in °C"
                    onChange={(e) => {setProvidedTemperature(e.target.value); setError("")}}
                    value={providedTemperature}
                />
            </Modal.Body>
            <Modal.Footer className="justify-content-center d-flex flex-column">
                <Button variant="primary rounded-3" onClick={handleTemperatureEntered}>
                    Confirm
                </Button>
                {error !== "" ? <h5 className="text-danger mt-3">{error}</h5> : <></>}
            </Modal.Footer>
        </Modal>
    );
};

export default ChangeTemperatureModal;