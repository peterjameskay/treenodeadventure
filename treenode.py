class TreeNode:
    
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node):
      self.choices.append(node)
  
  def traverse(self):
    story_node = self
    print(story_node.story_piece)
    while len(story_node.choices) != 0:
      choice = int(input("Enter 1 or 2 to continue the story: "))
      if choice != 1 or choice != 2:
        print('Please enter 1 or 2.')
      chosen_index = choice - 1
      chosen_child = story_node.choices[chosen_index]
      print(chosen_child.story_piece)
      story_node = chosen_child