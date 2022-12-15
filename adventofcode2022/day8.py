# Traverse each row back
# Traverse each column down
# Traverse each column up

class GridTrees:
    def __init__(self, lines):
        # Assume it's a square, initialize tree arrays
        self.rows = len(lines)
        self.columns = len(lines[0].rstrip())
        self.tree_heights = [[0 for i in range(self.columns)] for j in range(self.rows)]
        self.tree_visible = [[False for i in range(self.columns)] for j in range(self.rows)]
        for row, line in enumerate(lines):
            for column, tree_height in enumerate(line.rstrip()):
                self.tree_heights[row][column] = int(tree_height)

        self.left_view()
        self.right_view()
        self.top_view()
        self.bottom_view()

        self.scenic_scores = [[0 for i in range(self.columns)] for j in range(self.rows)]
        for row in range(self.rows):
            for column in range(self.columns):
                score = self.scenic_up(row, column) * self.scenic_down(row, column) * self.scenic_left(row, column) * self.scenic_right(row, column)
                self.scenic_scores[row][column] = score

    def left_view(self):
        # Look at each row
        for row in range(self.rows):
            current_height = -1  # Start with no blocking trees
            # From the left
            for column in range(self.columns):
                tree_height = self.tree_heights[row][column]
                if current_height < tree_height:  # If the tree is visible
                    self.tree_visible[row][column] = True
                    # Update current blocking height
                    current_height = tree_height

    def right_view(self):
        # Look at each row
        for row in range(self.rows):
            current_height = -1  # Start with no blocking trees
            # From the right
            for column in reversed(range(self.columns)):
                tree_height = self.tree_heights[row][column]
                if current_height < tree_height:  # If the tree is visible
                    self.tree_visible[row][column] = True
                    # Update current blocking height
                    current_height = tree_height

    def top_view(self):
        # Look at each column
        for column in range(self.columns):
            current_height = -1  # Start with no blocking trees
            # From the top
            for row in range(self.rows):
                tree_height = self.tree_heights[row][column]
                if current_height < tree_height:  # If the tree is visible
                    self.tree_visible[row][column] = True
                    # Update current blocking height
                    current_height = tree_height

    def bottom_view(self):
        # Look at each column
        for column in range(self.columns):
            current_height = -1  # Start with no blocking trees
            # From the bottom
            for row in reversed(range(self.rows)):
                tree_height = self.tree_heights[row][column]
                if current_height < tree_height:  # If the tree is visible
                    self.tree_visible[row][column] = True
                    # Update current blocking height
                    current_height = tree_height

    def scenic_up(self, row, column):
        tree_house_height = self.tree_heights[row][column]

        # From row up in this column
        visible_trees = 0
        for r in reversed(range(row)):
            tree_height = self.tree_heights[r][column]
            if tree_height < tree_house_height:
                visible_trees += 1
            elif tree_height >= tree_house_height:
                visible_trees += 1
                break

        return visible_trees

    def scenic_down(self, row, column):
        tree_house_height = self.tree_heights[row][column]

        # From row down in this column
        visible_trees = 0
        for r in range(row + 1, self.rows):
            tree_height = self.tree_heights[r][column]
            if tree_height < tree_house_height:
                visible_trees += 1
            elif tree_height >= tree_house_height:
                visible_trees += 1
                break

        return visible_trees

    def scenic_left(self, row, column):
        tree_house_height = self.tree_heights[row][column]

        # From column left in this row
        visible_trees = 0
        for c in reversed(range(column)):
            tree_height = self.tree_heights[row][c]
            if tree_height < tree_house_height:
                visible_trees += 1
            elif tree_height >= tree_house_height:
                visible_trees += 1
                break

        return visible_trees

    def scenic_right(self, row, column):
        tree_house_height = self.tree_heights[row][column]

        # From column right in this row
        visible_trees = 0
        for c in range(column + 1, self.columns):
            tree_height = self.tree_heights[row][c]
            if tree_height < tree_house_height:
                visible_trees += 1
            elif tree_height >= tree_house_height:
                visible_trees += 1
                break

        return visible_trees


def part1():
    with open("day8.input") as f:
        lines = list(f)
        grid_trees = GridTrees(lines)

        count = 0
        for row in grid_trees.tree_visible:
            for column in row:
                if column:
                    count += 1

        return count


def part2():
    with open("day8.input") as f:
        lines = list(f)
        grid_trees = GridTrees(lines)

        best = 0
        for row in grid_trees.scenic_scores:
            for score in row:
                if score > best:
                    best = score

        return best


def main():
    print(part1())
    print(part2())


if __name__ == "__main__":
    main()