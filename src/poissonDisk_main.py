from src.pygame_PoissonDisk import PygamePoissonDisk
from src.poisson_disk import PoissonDisk

if __name__ == "__main__":
    pygame_renderer = PygamePoissonDisk(800, 600)
    poisson_disk = PoissonDisk(800, 600, 100, 30)
    poisson_disk.poisson_disk_sampling()

    running = True
    while running:
        pygame_renderer.handle_events()

        pygame_renderer.clear_screen()
        pygame_renderer.draw_points(poisson_disk.samples)
        pygame_renderer.update_display()

        running = running and pygame_renderer.running

    PygamePoissonDisk.close()
