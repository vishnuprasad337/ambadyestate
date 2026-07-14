function formatNumber(number) {
  return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function animateNumber(element, targetNumber, duration) {
  const startTime = performance.now();
  function updateNumber(currentTime) {
    const elapsedTime = currentTime - startTime;
    const progress = Math.min(elapsedTime / duration, 1);
    element.innerText = formatNumber(Math.floor(progress * targetNumber));
    if (progress < 1) requestAnimationFrame(updateNumber);
  }
  requestAnimationFrame(updateNumber);
}

function initAmbadySite() {
  if (document.body?.dataset.ambadyInitialized === "true") return;
  document.body.dataset.ambadyInitialized = "true";

  const header = document.getElementById("header");
  const revealItems = document.querySelectorAll(".reveal-up, .reveal-left, .reveal-right, .scrollanimation, [data-aos]");
  const navLinks = document.querySelectorAll(".navbar-nav .nav-link");
  const sections = document.querySelectorAll("main [id]");
  const numberElements = document.querySelectorAll(".number");
  const heroSection = document.querySelector(".hero-section");

  const updateHeaderState = () => header?.classList.toggle("is-scrolled", window.scrollY > 40);

  const activateCurrentSection = () => {
    const scrollPosition = window.scrollY + 140;
    sections.forEach((section) => {
      const id = section.getAttribute("id");
      const top = section.offsetTop;
      const height = section.offsetHeight;
      const isActive = scrollPosition >= top && scrollPosition < top + height;
      navLinks.forEach((link) => {
        link.classList.toggle("active", link.getAttribute("href") === `#${id}` && isActive);
      });
    });
  };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add("is-visible");
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.15, rootMargin: "0px 0px -60px 0px" });

  revealItems.forEach((item, index) => {
    if (item.matches(".scrollanimation, [data-aos]") && !item.style.transitionDelay) {
      item.style.transitionDelay = `${Math.min((index % 4) * 90, 270)}ms`;
    }
    revealObserver.observe(item);
  });

  const numberObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      animateNumber(el, parseInt(el.dataset.target || "0", 10), parseInt(el.dataset.duration || "1200", 10));
      observer.unobserve(el);
    });
  }, { threshold: 0.65 });

  numberElements.forEach((el) => numberObserver.observe(el));

  if (heroSection) {
    const heroSliderElement = heroSection.querySelector(".hero-slider");
    const heroPagination = heroSection.querySelector(".hero-slider-pagination");
    const heroNext = heroSection.querySelector(".hero-slider-next");
    const heroPrev = heroSection.querySelector(".hero-slider-prev");
    const heroCurrent = heroSection.querySelector(".hero-slide-current");
    const heroTotal = heroSection.querySelector(".hero-slide-total");
    const heroProgressBar = heroSection.querySelector(".hero-progress-bar");
    const heroSlides = heroSliderElement?.querySelectorAll(".swiper-slide") || [];
    const totalSlides = heroSlides.length;

    const formatSlideNumber = (value) => value.toString().padStart(2, "0");
    const updateHeroProgress = (swiper) => {
      if (!totalSlides) return;
      const currentIndex = (swiper?.realIndex ?? 0) + 1;
      const progress = Math.min(currentIndex / totalSlides, 1);
      if (heroCurrent) heroCurrent.textContent = formatSlideNumber(currentIndex);
      if (heroTotal) heroTotal.textContent = formatSlideNumber(totalSlides);
      if (heroProgressBar) heroProgressBar.style.width = `${progress * 100}%`;
    };

    new Swiper(heroSliderElement, {
      loop: true,
      speed: 900,
      allowTouchMove: true,
      autoplay: {
        delay: 4500,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
      },
      pagination: {
        el: heroPagination,
        clickable: true,
      },
      navigation: {
        nextEl: heroNext,
        prevEl: heroPrev,
      },
      on: {
        init: updateHeroProgress,
        slideChange: updateHeroProgress,
      },
    });
  }

  updateHeaderState();
  activateCurrentSection();
  window.addEventListener("scroll", () => {
    updateHeaderState();
    activateCurrentSection();
  });
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initAmbadySite, { once: true });
} else {
  initAmbadySite();
}
