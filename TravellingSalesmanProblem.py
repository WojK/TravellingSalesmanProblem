import matplotlib.pyplot as plt
from GeneticAlgorithm import GeneticAlgorithm


cities = [('A', 2, 1), ('B', 9, 7), ('C', 6, 5), ('D', 1, 7), ('E', 3, 6 ), ('F', 5, 6), ('G', 4, 2), ('H', 10, 4), ('I', 7, 3), ('J', 8, 10)]
population = 120
mutation_prob = 0.001
iterations = 200


ag = GeneticAlgorithm(mutation_prob, population, cities, iterations)
ag.run()

scores = ag.iterations_scores
worst_route, best_route = ag.get_best_and_worst_chromosome()  



def plot_routes(cities1, cities2, title1, title2):
    x_values1 = [city[1] for city in cities1]
    y_values1 = [city[2] for city in cities1]

    x_values2 = [city[1] for city in cities2]
    y_values2 = [city[2] for city in cities2]

    fig, axs = plt.subplots(2, 2, figsize=(11, 7))

    axs[0, 0].plot(x_values1 + [x_values1[0]], y_values1 + [y_values1[0]], linestyle='-', linewidth=1, color='black')
    axs[0, 1].plot(x_values2 + [x_values2[0]], y_values2 + [y_values2[0]], linestyle='-', linewidth=1, color='blue')

    for c in cities1:
        axs[0, 0].scatter(c[1], c[2], c='red', marker='o', s=50)
        axs[0, 0].text(c[1], c[2], c[0], fontsize=14, ha='right')

    for c in cities2:
        axs[0, 1].scatter(c[1], c[2], c='red', marker='o', s=50)
        axs[0, 1].text(c[1], c[2], c[0], fontsize=14, ha='right')

    axs[0, 0].set_title(title1)
    axs[0, 0].set_xlabel('X')
    axs[0, 0].set_ylabel('Y')
    axs[0, 1].set_title(title2)
    axs[0, 1].set_xlabel('X')
    axs[0, 1].set_ylabel('Y')

    axs[0, 0].grid(True)
    axs[0, 1].grid(True)

    scores_min = [s[0] for s in scores]
    scores_avg = [s[1] for s in scores]
    scores_max = [s[2] for s in scores]
    graph_stats_x = [i for i in range(iterations)]

    axs[1, 0].set_xlabel("Populacja")
    axs[1, 0].set_ylabel("Przystosowanie")
    axs[1, 0].set_title("Wizualizacja wynikow przystosowania kolejnych populacji")

    axs[1, 0].plot(graph_stats_x, scores_min, label="Min")
    axs[1, 0].plot(graph_stats_x, scores_avg, label="Max")
    axs[1, 0].plot(graph_stats_x, scores_max, label="Avg")

    axs[1, 0].legend()

    axs[1, 1].axis('off')

    plt.tight_layout()
    plt.savefig("./wyniki.png")
    plt.show()



plot_routes(worst_route.cities, best_route.cities, "Najgorszy osobnik", "Najlepszy osobnik")
