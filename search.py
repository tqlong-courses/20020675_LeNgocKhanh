# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    stack = util.Stack()  # Create an empty stack
    stack.push((problem.getStartState(), []))  # Push the start state and an empty list of actions onto the stack
    visited = set()  # Create an empty set to store visited states

    while not stack.isEmpty():
        state, actions = stack.pop()  # Pop a state and its corresponding actions from the stack

        if problem.isGoalState(state):  # If the state is the goal state, return the list of actions
            return actions

        if state not in visited:  # If the state has not been visited
            visited.add(state)  # Mark the state as visited
            successors = problem.getSuccessors(state)  # Get the successors of the state

            for successor, action, _ in successors:
                stack.push((successor, actions + [action]))  # Push the successor state and the new action onto the stack

    return []  # Return an empty list if no path to the goal state is found
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    queue = util.Queue()  # Create an empty queue
    queue.push((problem.getStartState(), []))  # Push the start state and an empty list of actions onto the queue
    visited = set()  # Create an empty set to store visited states

    while not queue.isEmpty():
        state, actions = queue.pop()  # Pop a state and its corresponding actions from the queue

        if problem.isGoalState(state):  # If the state is the goal state, return the list of actions
            return actions

        if state not in visited:  # If the state has not been visited
            visited.add(state)  # Mark the state as visited
            successors = problem.getSuccessors(state)  # Get the successors of the state

            for successor, action, _ in successors:
                queue.push((successor, actions + [action]))  # Push the successor state and the new action onto the queue

    return []  # Return an empty list if no path to the goal state is found
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    priorityQueue = util.PriorityQueue()  # Create an empty priority queue
    priorityQueue.push((problem.getStartState(), [], 0), 0)  # Push the start state, an empty list of actions, and the cost as the priority
    visited = set()  # Create an empty set to store visited states

    while not priorityQueue.isEmpty():
        state, actions, cost = priorityQueue.pop()  # Pop a state, its corresponding actions, and the cost from the priority queue

        if problem.isGoalState(state):  # If the state is the goal state, return the list of actions
            return actions

        if state not in visited:  # If the state has not been visited
            visited.add(state)  # Mark the state as visited
            successors = problem.getSuccessors(state)  # Get the successors of the state

            for successor, action, stepCost in successors:
                totalCost = cost + stepCost
                priorityQueue.push((successor, actions + [action], totalCost), totalCost)  # Push the successor state, the new action, and the total cost as the priority

    return []  # Return an empty list if no path to the goal state is found
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    priorityQueue = util.PriorityQueue()  # Create an empty priority queue
    priorityQueue.push((problem.getStartState(), [], 0), 0)  # Push the start state, an empty list of actions, and the cost as the priority
    visited = set()  # Create an empty set to store visited states

    while not priorityQueue.isEmpty():
        state, actions, cost = priorityQueue.pop()  # Pop a state, its corresponding actions, and the cost from the priority queue

        if problem.isGoalState(state):  # If the state is the goal state, return the list of actions
            return actions

        if state not in visited:  # If the state has not been visited
            visited.add(state)  # Mark the state as visited
            successors = problem.getSuccessors(state)  # Get the successors of the state

            for successor, action, stepCost in successors:
                totalCost = cost + stepCost
                heuristicCost = totalCost + heuristic(successor, problem)  # Calculate the heuristic cost
                priorityQueue.push((successor, actions + [action], totalCost), heuristicCost)  # Push the successor state, the new action, and the total cost + heuristic as the priority

    return []  # Return an empty list if no path to the goal state is found
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
