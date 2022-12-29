
const stopCamera = (webVideo: any, ctx: any, camera: any) => {
    if (!webVideo.value?.srcObject) {
        return
    }
    const stream = webVideo.value.srcObject as MediaStream
    const tracks = stream.getTracks()
    tracks.forEach((track) => {
        track.stop()
    })
    webVideo.value.srcObject = null
    ctx.value.clearRect(0, 0, 1280, 720)
    camera.value?.stop()
    return { webVideo, ctx, camera }
}


export default stopCamera;