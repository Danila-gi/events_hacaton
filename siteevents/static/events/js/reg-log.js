document.addEventListener('DOMContentLoaded', function () {
    let lastMouseX = 0;
    let lastMouseY = 0;

    function updateEyeRotation(mouseX, mouseY) {
        const person = document.querySelector(".reg-log-form__title");
        const rect = person.getBoundingClientRect();

        const personX = rect.left + rect.width / 2;
        const personY = rect.top + rect.height / 2;

        const angleDeg = getAngle(mouseX, mouseY, personX, personY);

        const eyes = document.querySelectorAll(".reg-log-glaz");
        eyes.forEach(eye => {
            eye.style.transform = `rotate(${90 + angleDeg}deg)`;
        });
    }
   

    document.addEventListener('mousemove', (e) => {
        lastMouseX = e.clientX;
        lastMouseY = e.clientY;
        updateEyeRotation(lastMouseX, lastMouseY);
    });

    document.addEventListener('scroll', () => {
        updateEyeRotation(lastMouseX, lastMouseY);
    });
});

function getAngle(cx, cy, ex, ey) {
    const dy = ey - cy,
          dx = ex - cx,
          rad = Math.atan2(dy, dx),
          deg = rad * 180 / Math.PI;
    return deg;
}
