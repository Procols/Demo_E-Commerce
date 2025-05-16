document.addEventListener("DOMContentLoaded", function () {
    const videos = document.querySelectorAll(".insta-video-card video");

    videos.forEach((video) => {
      // Desktop: Play on hover, pause on leave
      video.addEventListener("mouseenter", () => {
        video.muted = true;
        video.play();
      });

      video.addEventListener("mouseleave", () => {
        video.pause();
        video.currentTime = 0; // Optional: reset to start
      });

      // Mobile: Play on first touch
      video.addEventListener("touchstart", () => {
        if (video.paused) {
          video.muted = true;
          video.play();
        } else {
          video.pause();
          video.currentTime = 0;
        }
      });
    });
  });

document.addEventListener("DOMContentLoaded", function () {
    const videos = document.querySelectorAll(".review-video-card video");

    videos.forEach((video) => {
      // Desktop: Play on hover, pause on leave
      video.addEventListener("mouseenter", () => {
        video.muted = true;
        video.play();
      });

      video.addEventListener("mouseleave", () => {
        video.pause();
        video.currentTime = 0; // Optional: reset to start
      });

      // Mobile: Play on first touch
      video.addEventListener("touchstart", () => {
        if (video.paused) {
          video.muted = true;
          video.play();
        } else {
          video.pause();
          video.currentTime = 0;
        }
      });
    });
  });