export interface Alert {
    id: number,
    action: string,
    cause: string,
    room: number,
    date: string
}

export interface Room {
    id: number,
    name: string,
    preferred_temp?: number,
    humidity: number,
    temperature: number,
    pressure: number,
    time: string
}

export interface Plots {
    temperature: string,
    humidity: string,
    pressure: string
}