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
    preferredTemp?: number,
    humidity: number,
    temperature: number,
    time: string
}

export interface Plots {
    temperature: string,
    humidity: string,
    pressure: string
}