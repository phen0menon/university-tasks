#include <iostream>
#include <memory>

template<typename Derived, typename Base, typename Del>
std::unique_ptr<Derived, Del> dynamic_unique_ptr_cast(std::unique_ptr<Base, Del>&& ptr) {
	if (Derived *result = dynamic_cast<Derived *>(ptr.get())) {
		ptr.release();
		return std::unique_ptr<Derived, Del>(result, std::move(ptr.get_deleter()));
	}
	return std::unique_ptr<Derived, Del>(nullptr, ptr.get_deleter());
}

class Base {
public:
	Base(const char* _title): title(_title) {};
	virtual void getTitle() {
		std::cout << "Base => " << title << "\n";
	}
	virtual ~Base() {
		std::cout << "Base's destructor called with title " << title << "\n";
	}

protected:
	const char* title;
};

class Derived: public Base {
public:
	Derived(const char* _title): Base(_title) {};
	virtual void getTitle() {
		std::cout << "Derived => " << title << "\n";
	}
	virtual ~Derived() {
		std::cout << "Derived's destructor called with title " << title << "\n";
	}
};

int main() {
	auto derived = std::make_unique<Derived>("0xFFF");
	derived->getTitle();

	std::unique_ptr<Base> base = std::move(derived);
	base->getTitle();

	auto derived_copy =	dynamic_unique_ptr_cast<Derived>(std::move(base));
	derived_copy->getTitle();

	std::unique_ptr<Base> base_copy = std::make_unique<Derived>("0xCCC");
	base_copy->getTitle();

	return 0;
}