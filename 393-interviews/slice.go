type Container struct {
	data []int
	length int
	capacity int
}

func Insert(container Container*, location int, value int) {
	length := container.length
	CheckLength(container, length)
	length++
	for i := length - 1; i > location; i-- {
		container.data[i] = container.data[i - 1]
	}
	container.data[location] = value
	container.length = length
}

func CheckLength(Container* container, int length) {
	if (length < container.capacity) {
		return
	}

	length = length << 1
	data := make([]int, length)
	for i := 0; i < container.length; i++ {
		data[i] = container.data[i]
	}
	container.data = data
	container.capacity = length
}