import pygame
import classes
import sys
import random
pygame.init()
screen = pygame.display.set_mode((600,600))
player = classes.character([300,300],(255,95,95))
clock = pygame.time.Clock()
movement_particles = []
while True:
	screen.fill((95,95,100))
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			pygame.quit()
			sys.exit()
	keys = pygame.key.get_pressed()
	if (keys[pygame.K_UP]):
		player.pos[1] -= 5
		for i in range(5):
			movement_particles.append(classes.particle([player.character.center[0],player.character.bottom],random.randint(-5,5),5,50))
	elif (keys[pygame.K_DOWN]):
		player.pos[1] += 5
		for i in range(5):
			movement_particles.append(classes.particle([player.character.center[0],player.character.top-20],random.randint(-5,5),-5,50))
	if (keys[pygame.K_LEFT]):
		player.pos[0] -= 5
		for i in range(5):
			movement_particles.append(classes.particle([player.character.bottomright[0],player.character.center[1]],5,random.randint(-5,5),50))
	elif (keys[pygame.K_RIGHT]):
		player.pos[0] += 5
		for i in range(5):
			movement_particles.append(classes.particle([player.character.bottomleft[0]-20,player.character.center[1]],5,random.randint(-5,5),50))
	player.update()
	player.draw(screen)
	for particle in movement_particles:
		status = particle.update(clock)
		if (status == 1):
			movement_particles.remove(particle)
		else:
			particle.draw(screen)
	pygame.display.update()
	clock.tick(60)