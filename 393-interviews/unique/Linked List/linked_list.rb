class Node
    attr_accessor :data, :next_node
  
    def initialize(data)
      @data = data
      @next_node = nil
    end
  end
  
  class LinkedList
    def initialize
      @head = nil
    end
  
    def append(data)
      new_node = Node.new(data)
      if @head.nil?
        @head = new_node
      else
        current = @head
        while current.next_node
          current = current.next_node
        end
        current.next_node = new_node
      end
    end
  
    def display
      current = @head
      while current
        print "#{current.data} -> "
        current = current.next_node
      end
      puts "nil"
    end
  
    def delete(data)
      if @head.nil?
        puts "List is empty, cannot delete."
        return
      end
  
      if @head.data == data
        @head = @head.next_node
        return
      end
  
      current = @head
      while current.next_node
        if current.next_node.data == data
          current.next_node = current.next_node.next_node
          return
        end
        current = current.next_node
      end
  
      puts "Data not found in the list."
    end
  end
  
  my_list = LinkedList.new
  my_list.append(1)
  my_list.append(2)
  my_list.append(3)
  
  puts "Original linked list:"
  my_list.display
  
  my_list.delete(2)
  
  puts "Linked list after deleting 2:"
  my_list.display
  