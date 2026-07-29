function initAmbadySliders() {
  if (document.body?.dataset.ambadySlidersInitialized === "true") return;
  document.body.dataset.ambadySlidersInitialized = "true";

  const partnerSlider = document.querySelector(".swiperPartner");
  if (partnerSlider) {
    new Swiper(partnerSlider, {
      speed: 900,
      loop: true,
      centeredSlides: true,
      grabCursor: true,
      autoplay: {
        delay: 2200,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      breakpoints: {
        0: {
          slidesPerView: 1.4,
          spaceBetween: 18,
        },
        768: {
          slidesPerView: 2.4,
          spaceBetween: 24,
        },
        1024: {
          slidesPerView: 3.2,
          spaceBetween: 28,
        },
      },
      pagination: {
        el: partnerSlider.querySelector(".swiper-pagination"),
        clickable: true,
      },
    });
  }

  const testimonialSlider = document.querySelector(".swiperTestimonials");
  if (testimonialSlider) {
    new Swiper(testimonialSlider, {
      speed: 850,
      loop: true,
      autoHeight: true,
      spaceBetween: 18,
      grabCursor: true,
      autoplay: {
        delay: 4200,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      pagination: {
        el: testimonialSlider.querySelector(".swiper-pagination"),
        clickable: true,
      },
    });
  }

  const activitiesSlider = document.querySelector(".activities-slider");
  if (activitiesSlider) {
    new Swiper(activitiesSlider, {
      speed: 800,
      loop: true,
      spaceBetween: 24,
      autoplay: {
        delay: 5200,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      pagination: {
        el: activitiesSlider.querySelector(".activities-slider-pagination"),
        clickable: true,
      },
      navigation: {
        nextEl: activitiesSlider.querySelector(".activities-slider-next"),
        prevEl: activitiesSlider.querySelector(".activities-slider-prev"),
      },
    });
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initAmbadySliders, { once: true });
} else {
  initAmbadySliders();
}
